import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Home = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const result = await axios.get('http://localhost:5000/patients');
        setData(result.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="home">
      <h2>Home</h2>
      <ul>
        {data.map((patient, index) => (
          <li key={index}>{patient.name} - {patient.disease}</li>
        ))}
      </ul>
    </div>
  );
};

export default Home;
