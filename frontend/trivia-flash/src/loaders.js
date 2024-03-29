async function randomCardLoader({ request, params }) {
  const res = await fetch('http://127.0.0.1:5555/cards/random')
    .then(resp => resp.json())
  return res
}

export {
  randomCardLoader
}