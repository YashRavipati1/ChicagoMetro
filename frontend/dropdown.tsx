import React, { useState, useEffect } from 'react';
import station_names from '../datasets/secondary.json';

const DropdownComponent: React.FC = () => {
    const [options, setOptions] = useState<string[]>([]);
  
    useEffect(() => {
      // Extract values from the JSON data and set the options state
      setOptions(Object.values(station_names));
    }, []);
  
    const handleDropdownChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
      const selectedOption = event.target.value;
      console.log(selectedOption); // Do something with the selected option
    };
  
    return (
      <div>
        <label htmlFor="dropdown">Select an option:</label>
        <select id="dropdown" onChange={handleDropdownChange}>
          {options.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      </div>
    );
  };
  
  export default DropdownComponent;