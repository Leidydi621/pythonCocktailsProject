import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import { CocktailsPage } from './pages/CocktailsPage'
import { CocktailForm } from './pages/CosktailForm'
import { Navigation } from './components/Navigation'

function App() {
  return (
    <BrowserRouter>
    <Navigation/>
    <Routes>
      <Route path='/' element={<Navigate to='/cocktails'/>}/>
      <Route path='/cocktails' element={<CocktailsPage/>}/>
      <Route path='/cocktail-create' element={<CocktailForm/>}/>
    </Routes>
    </BrowserRouter>
  )
}

export default App