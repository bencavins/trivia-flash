import './ImageCard.css'
import { useState } from 'react'

export default function ImageCard({ img_url, answer }) {
  const [msg, setMsg] = useState("")

  function handleSubmit(event) {
    event.preventDefault()
    if (event.target['user-answer'].value.toLowerCase() == answer.toLowerCase()) {
      setMsg('Correct!')
    } else {
      setMsg(`Incorrect! (answer: ${answer})`)
    }
  }

  return (
    <div>
      <img src={img_url} />
      {msg ? <p>{msg}</p> : null}
      <form onSubmit={handleSubmit}>
        <label>Name the movie: </label>
        <input type="text" name="user-answer" />
        <input type="submit" />
      </form>
    </div>
  )
}