import {useState} from "react";
import axios from "axios";
import "./App.css";

function App(){

const [query,setQuery]=useState("");
const [recommendations,setRecommendations]=useState([]);
const [loading,setLoading]=useState(false);

async function getRecommendations(){

try{

setLoading(true);

const response=await axios.get(
`http://127.0.0.1:8000/recommend?query=${query}`
);

setRecommendations(
response.data.recommendations
);

}
catch(error){

console.log(error);

}
finally{

setLoading(false);

}

}

return(

<div className="container">

<h1>AI Movie Recommendation System</h1>

<input
value={query}
onChange={(e)=>setQuery(e.target.value)}
placeholder="Describe movies"
/>

<button
onClick={getRecommendations}
>
Recommend
</button>

{loading && <h3>Loading...</h3>}

<div className="cards">

{recommendations.map(
(movie,index)=>

<div
className="card"
key={index}
>

{movie}

</div>

)}

</div>

</div>

)

}

export default App;