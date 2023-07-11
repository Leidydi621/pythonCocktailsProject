import { useNavigate } from "react-router-dom";
import style from './Card.module.css'

export function Card({ name, categoryName, glass, ingredients, instructions, img }){
    // const navigate = useNavigate();

    return (
        <div className={style.bodyCard}>   
          <div className={style.container}>
            <div className={style.card} id = 'card'>
              <div className={style.img}>
                    <img src ={img} alt= "img not found" width= "150px" height= "150px"/>
                </div>
                <div className={style.info}>
                    <h3>{name}</h3>
                    <h4>Category: {categoryName}</h4>
                    <h4>Glass: {glass}</h4>
                    <h5>ingredients: </h5>
                    <p>{ingredients}</p>
                    <h5>Instructions: </h5>
                    <p>{instructions}</p> 
                </div>
             </div>
         </div>
       </div>
    )
}