import { PredictionResult } from '../App'
import './ResultsTable.css'

interface ResultsTableProps {
  results: PredictionResult[]
}

function ResultsTable({ results }: ResultsTableProps) {
  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 0.8) return 'high'
    if (confidence >= 0.5) return 'medium'
    return 'low'
  }

  const formatConfidence = (confidence: number) => {
    return (confidence * 100).toFixed(1) + '%'
  }

  return (
    <div className="results-table-container">
      <h2>분석 결과</h2>
      <div className="table-wrapper">
        <table className="results-table">
          <thead>
            <tr>
              <th>파일명</th>
              <th>예측 품종</th>
              <th>신뢰도</th>
              <th>상세 예측</th>
            </tr>
          </thead>
          <tbody>
            {results.map((result, index) => (
              <tr key={index}>
                <td className="filename-cell">{result.filename}</td>
                <td className="prediction-cell">
                  <span className="prediction-badge">{result.prediction}</span>
                </td>
                <td>
                  <span className={`confidence-badge ${getConfidenceColor(result.confidence)}`}>
                    {formatConfidence(result.confidence)}
                  </span>
                </td>
                <td>
                  <div className="all-predictions">
                    {result.all_predictions?.map((pred, idx) => (
                      <span key={idx} className="prediction-item">
                        {pred.label}: {(pred.confidence * 100).toFixed(1)}%
                      </span>
                    ))}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

export default ResultsTable
