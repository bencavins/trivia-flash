import { useState } from 'react'
import { useLoaderData } from 'react-router-dom'
import './App.css'
import ImageCard from './ImageCard'

function App() {
  const [count, setCount] = useState(0)
  const cardData = useLoaderData()

  return (
    <>
      <h1>Trivia Flash</h1>
      <ImageCard {...cardData} />
    </>
  )
}

export default App
