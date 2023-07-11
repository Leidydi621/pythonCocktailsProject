import axios from 'axios';

export const GET_COCKTAILS = 'GET_COCKTAILS'


export const GetAllCocktails = () => {
    return axios.get('http://localhost:8000/cocktails/api/v1/cocktails/')
}

