import React from 'react';
import './App.css';

function App() {

  const [data, setData] = React.useState({
    distance: 0,
    path_string: "",
    graph: "",
  });

  const [start, setStart] = React.useState("");
  const [end, setEnd] = React.useState("");
  const [header, setHeader] = React.useState("Please Input the Start and End Stations");

  const handleChangeStart = (event: { target: { value: string }; }) => {
    setStart(event.target.value);
  }

  const handleChangeEnd = (event: { target: { value: string }; }) => {
    setEnd(event.target.value);
  }

  const HandleClick = () => {
    setHeader(`Path from ${start} to ${end}`);
    console.log(start, end);
    console.log(`http://localhost:5000/calculate_path/${start}/${end}`);
    fetch(`http://localhost:5000/calculate_path/${start}/${end}`, {
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
      console.log(data);
      setData({
        distance: data.distance,
        path_string: data.path_string,
        graph: data.graph || "", // Set data.graph to empty string if data.graph is null or undefined
      });
    })
    .catch((error) => {
      console.error('Error fetching data:', error);
      setData({
        distance: 0,
        path_string: "Incorrect Station Name.",
        graph: "", // Clear the image in case of an error
      });
    });
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>{header}</h1>
        {/* Calling a data from setdata for showing */}
        <input
          type="text"
          value={start}
          onChange={handleChangeStart}
          className="input-field"
        />
        <input
          type="text"
          value={end}
          onChange={handleChangeEnd}
          className="input-field"
        />

        <button onClick={HandleClick} className="update-button">
          Find Path
        </button>

        <p>{data.path_string}</p>
        <p>Distance: {data.distance.toFixed(2)}</p>
        {data.graph && (
          <img key={data.graph} src={`data:image/png;base64,${data.graph}`} alt="" />
        )}
      </header>
    </div>
  );
}

export default App;
