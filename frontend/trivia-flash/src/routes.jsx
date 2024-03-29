import App from "./components/App"
import { randomCardLoader } from './loaders'

const routes = [
  {
    path: '/',
    element: <App />,
    loader: randomCardLoader
  }
]

export default routes