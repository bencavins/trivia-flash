import './ImageCard.css'

export default function ImageCard({ img_url, answer }) {
  return (
    <div>
      <img src={img_url} />
      <form>
        <label>Name the movie: </label>
        <input type="text" />
        <input type="submit" />
      </form>
    </div>
  )
}