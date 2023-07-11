import {Link} from 'react-router-dom'

export function Navigation() {
  return (
    <div>
        <Link to='/cocktails'>
            <h1>Cocktail App</h1>
        </Link>
        <Link to='/cocktail-create'>
            Crea tu Cocktail
        </Link>
    </div>
  )
}

