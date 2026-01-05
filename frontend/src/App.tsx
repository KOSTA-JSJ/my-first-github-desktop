import { useState } from 'react'
import FileUpload from './components/FileUpload'
import ResultsTable from './components/ResultsTable'
import ExportButton from './components/ExportButton'
import './App.css'

export interface PredictionResult {
  filename: string
  prediction: string
  confidence: number
  all_predictions?: Array<{ label: string; confidence: number }>
}

function App() {
  const [results, setResults] = useState<PredictionResult[]>([])
  const [loading, setLoading] = useState(false)

  const handlePredict = async (files: File[]) => {
    setLoading(true)
    try {
      const formData = new FormData()
      
      if (files.length === 1) {
        // 단일 이미지 예측
        formData.append('file', files[0])
        const response = await fetch('http://localhost:8000/predict', {
          method: 'POST',
          body: formData,
        })
        
        if (!response.ok) {
          throw new Error('예측 실패')
        }
        
        const data = await response.json()
        setResults([data])
      } else {
        // 배치 예측
        files.forEach(file => {
          formData.append('files', file)
        })
        
        const response = await fetch('http://localhost:8000/batch', {
          method: 'POST',
          body: formData,
        })
        
        if (!response.ok) {
          throw new Error('배치 예측 실패')
        }
        
        const data = await response.json()
        setResults(data.results)
      }
    } catch (error) {
      console.error('예측 오류:', error)
      alert('예측 중 오류가 발생했습니다.')
    } finally {
      setLoading(false)
    }
  }

  const handleExport = async () => {
    if (results.length === 0) {
      alert('내보낼 결과가 없습니다.')
      return
    }

    try {
      const response = await fetch('http://localhost:8000/export/xlsx', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ results }),
      })

      if (!response.ok) {
        throw new Error('내보내기 실패')
      }

      const blob = await response.blob()
      const url = window.URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = 'rice_variety_results.xlsx'
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(url)
      document.body.removeChild(a)
    } catch (error) {
      console.error('내보내기 오류:', error)
      alert('Excel 내보내기 중 오류가 발생했습니다.')
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>🌾 RiceVarietyVision</h1>
        <p className="subtitle">쌀 품종 이미지 분류 시스템</p>
      </header>

      <div className="app-content">
        <FileUpload onPredict={handlePredict} loading={loading} />
        
        {results.length > 0 && (
          <>
            <ResultsTable results={results} />
            <ExportButton onExport={handleExport} />
          </>
        )}
      </div>
    </div>
  )
}

export default App
