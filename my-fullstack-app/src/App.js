import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


function App() {
  const [inputText, setInputText] = useState('');
  const [tableData, setTableData] = useState([]);
 const [selectedFile, setSelectedFile] = useState(null);
const [uniqueTypes,setUniqueTypes]= useState([]);
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleInputChange = (e) => {
    setInputText(e.target.innerText);
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post('http://localhost:5000/process', { text: inputText });
      console.log(response);
      setTableData(response.data.tableData);
      setUniqueTypes( [...new Set(response.data.tableData.map(row => row.type))]);
    } catch (error) {
        // error?.message?error?.message:
        toast.error("This AI model does not structurize this type of input ", {
        position: 'top-right',
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
      console.error('There was an error processing your request', error);
    }
  };
   const handleUpload = async () => {
       const formData = new FormData();
           if (selectedFile) {
      // You can use FormData to send the file to the server
      console.log("form",formData)
      formData.append('file', selectedFile);
      setSelectedFile(null);
    }
    try {
        const config = {
          headers: {
            'Content-Type': 'multipart/form-data',  // Set Content-Type
            'enctype': 'multipart/form-data',       // Set enctype
          },
        };
      const response = await axios.post('http://localhost:5000/upload', formData,config);
      console.log("reached here",response);
      setTableData(response.data.tableData);
      setUniqueTypes([...new Set(response.data.tableData.map(row => row.type))]);

// setTableData(response.data.tableData);
      console.log(tableData.map(row => row.type))
    } catch (error) {
        toast.error("This AI model does not structurize this type of input ", {
        position: 'top-right',
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
      console.error('There was an error processing your request', error);
    }
  };

  return (
      <div className="App">
          <ToastContainer />
          <div className="inputWrapper">
              <div contentEditable="true" className="input" onInput={handleInputChange}></div>
              <button onClick={handleSubmit}>Submit</button>
          </div>
          <div className="inputWrapper">
              <input type="file" name="file" id="file" onChange={handleFileChange}/>
              <input type="button" onClick={handleUpload} value="submit"/>
          </div>
          <div>
              {/* Step 2 and 3: Create tables for each unique type and populate with rows */}
             {uniqueTypes.map((type, typeIndex) => {
        // Step 4: Find the unique columns for the current type
        const uniqueColumns = [...new Set(
          tableData
            .filter(row => row.type === type)
            .map(filteredRow => Object.keys(filteredRow).filter(column => column !== 'type'))
            .flat()
        )];
        const flag = type !== "NA";
        return (
          <div key={typeIndex} className="table-container">
            <h2 style={{display:flag?"hidden":"visible"}}>{type} Table</h2>
            <table>
              <thead>
                <tr>
                  {/* Use the unique columns for the current type */}
                  {uniqueColumns.map((column, columnIndex) => <th key={columnIndex}>{column}</th>)}
                </tr>
              </thead>
              <tbody>
                {/* Populate rows based on the type */}
                {tableData
                  .filter(row => row.type === type)
                  .map((filteredRow, rowIndex) => (
                    <tr key={rowIndex}>
                      {/* Use the unique columns for the current type */}
                      {uniqueColumns.map((column, columnIndex) => (
                        <td key={columnIndex}>{filteredRow[column]}</td>
                      ))}
                    </tr>
                  ))}
              </tbody>
            </table>
          </div>
        );
      })}
          </div>
      </div>
  );
}

export default App;


// increase the input box size
// submit should be larger and to the right side
//