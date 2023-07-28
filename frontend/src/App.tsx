import { useState } from 'react';
import Select from 'react-select';
import './App.css';

interface OptionType {
  value: string;
  label: string;
}

function App(this: any) {

  const options: OptionType[] = [
    { value: 'Nishi-magome', label: 'Nishi-magome' },
    { value: 'Magome', label: 'Magome' },
    { value: 'Ichigaya', label: 'Ichigaya' }
  ]

  const [data, setData] = useState({
    distance: 0,
    path_string: "",
    graph: "",
  });

  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [header, setHeader] = useState("Please Input the Start and End Stations");

  // const handleChangeStart = (event: { target: { value: string }; }) => {
  //   setStart(event.target.value);
  // }

  // const handleChangeEnd = (event: { target: { value: string }; }) => {
  //   setEnd(event.target.value);
  // }

  const handleChangeStartSelect = (selectedOption: OptionType | null) => {
    if (selectedOption === null) {
      return;
    }
    setStart(selectedOption['value']);
    console.log(`Option selected:`, selectedOption['value']);
  };
  const handleChangeEndSelect = (selectedOption: OptionType | null) => {
    if (selectedOption === null) {
      return;
    }
    setEnd(selectedOption['value']);
    console.log(`Option selected:`, selectedOption['value']);
  };
  const customStyles = {
    control: (base: any, state: any) => ({
      ...base,
      background: "black",
      borderRadius: state.isFocused ? "3px 3px 0 0" : 3,
      borderColor: state.isFocused ? "white" : "gray",
      "&:hover": {
        borderColor: state.isFocused ? "gray" : "white"
      },
      color: state.selectProps.inputValue ? 'blue' : 'black'
    }),
    input: (base: any) => ({
      ...base,
      color: 'white',
    }),
    option: (provided: any, base: any) => ({
      ...provided,
      backgroundColor: base.isFocused ? "gray" : "black",
    }),
    singleValue: (provided: any) => ({
      ...provided,
      color: 'white',
    }),
    menu: (base: any) => ({
      ...base,
      borderRadius: 2,
      marginTop: 0,
    }),
    menuList: (base: any) => ({
      ...base,
      padding: 0,
      borderRadius: 2,
    })
  };

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
        {/* <input
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
        /> */}
        <Select 
          options={options}
          onChange={handleChangeStartSelect}
          placeholder={'Starting Station'}
          className="input-field"
          styles={customStyles}
        />
        <Select 
          options={options}
          onChange={handleChangeEndSelect}
          placeholder={'Destination Station'}
          className="input-field"
          styles={customStyles}
        />

        <button onClick={HandleClick} className="update-button">
          Find Path
        </button>
        <div style={{whiteSpace: "pre-wrap"}} id='path-text'>
          <p>{data.path_string}</p>
          <p>Distance: {data.distance.toFixed(2)} km</p>
        </div>
        {data.graph && (
          <img key={data.graph} src={`data:image/png;base64,${data.graph}`} alt="" />
        )}
      </header>
    </div>
  );
}

export default App;
