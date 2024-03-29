import './ImageCard.css'
import { useState } from 'react'

export default function ImageCard({ img_url, answer }) {
  const [hasAnswered, setHasAnswered] = useState(false)
  const [isCorrect, setIsCorrect] = useState()

  function handleSubmit(event) {
    event.preventDefault()
    setHasAnswered(true)
    setIsCorrect(event.target['user-answer'].value.toLowerCase() == answer.toLowerCase())
  }

  const cardRespose = (
    <div className="card-response">
      {isCorrect ? 
        <p style={{color: 'green'}}>Correct!</p> 
      : <p style={{color: 'red'}}>Incorrect! The answer is {answer}</p>}
      <a href="/">Next Question</a>
    </div>
  )

  return (
    <div>
      <img src={img_url} />
      {hasAnswered ? cardRespose : null}
      <form onSubmit={handleSubmit}>
        <label>Name the movie: </label>
        <input type="text" name="user-answer" />
        <input type="submit" />
      </form>
    </div>
  )
}