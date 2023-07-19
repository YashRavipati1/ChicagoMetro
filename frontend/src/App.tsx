import React from 'react';
import './App.css';

function App() {

  const [data, setData] = React.useState({
    distance: 0,
    path_string: "",
    graph: new Image(),
  });

  React.useEffect(() => {
    fetch('http://localhost:5000/calculate_path/A01/G13', {
      method: 'GET',
    }).then((res) => {
      if (res.ok) {
        return res.json();
      } else {
        console.log(res);
        return {
          distance: 20,
          path_string: "Monkey",
        }
      }
    })
    .then((data) => {
      setData({
        distance: data.distance,
        path_string: data.path_string,
        graph: data.graph,
      });
    })
  }, []);
  

  return (
    <div className="App">
            <header className="App-header">
                <h1>O Noah, O Noah, wherefore art thou Noah</h1>
                {/* Calling a data from setdata for showing */}
                <p>{data.distance}</p>
                <p>{data.path_string}</p>
                {data.graph && (
                  <img src={`data:image/png;base64,${data.graph}`} alt="Error with img" />
                )}
            </header>
        </div>
  );
}

export default App;
