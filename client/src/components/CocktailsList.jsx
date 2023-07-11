import { useEffect, useState } from "react";
import { GetAllCocktails }  from '../api/cocktails.api.js'
import {Card} from './Card.jsx'


export function CocktailsList() {

  const [cocktails, setCocktails] = useState([]);


    useEffect(() => {
        async function loadCocktails() {
            const res = await GetAllCocktails()
            setCocktails(res.data)
        }
        loadCocktails()
    }, [])

  return (
    <div>
      {cocktails.map(e => (
        <Card 
          key={e.id}
          img={e.img}
          name={e.name}
          categoryName={e.categoryName}
          glass={e.glass}
          ingredients={e.ingredients}
          instructions={e.instructions}
         />
      ))}
    </div>
  )
}

