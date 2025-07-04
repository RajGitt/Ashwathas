import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
  axios.get('https://ashwathas.onrender.com/products') // ✅ Correct endpoint
    .then(res => setProducts(res.data))
    .catch(err => console.error("Failed to fetch products:", err));
}, []);

  return (
    <div className="bg-[#98be91] min-h-screen text-gray-900 font-serif">
      <header className="bg-[#76a06a] p-4 flex justify-between items-center">
        <div className="text-2xl font-bold text-[#062905]">Ashwathas</div>
        <nav className="space-x-4">
          <button className="text-white">Home</button>
          <button className="text-white">Shop</button>
          <button className="text-white">Contact</button>
        </nav>
      </header>

      <section className="h-screen flex items-center justify-center bg-[#76a06a]">
        <div className="text-center">
          <h1 className="text-6xl font-bold text-[#062905]">Ashwathas</h1>
          <p className="mt-4 italic text-xl text-white">“Rooted in Legacy, Styled for Eternity”</p>
        </div>
      </section>

      <section className="p-8 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.map(p => (
          <div key={p.id} className="bg-white p-4 rounded shadow text-center">
            <img src={p.image} alt={p.name} className="h-48 w-full object-cover rounded" />
            <h2 className="mt-2 text-lg font-semibold">{p.name}</h2>
            <p className="text-gray-600">Sizes: {p.sizes.join(', ')}</p>
            <p className="mt-1 font-bold">₹{p.price}</p>
            <div className="mt-2 flex justify-center space-x-4">
              <button>♥</button>
              <button>🛒</button>
            </div>
          </div>
        ))}
      </section>

      <footer className="bg-[#76a06a] p-6 text-center text-white">
        <p>📍 123 Ashwatha St, India</p>
        <p>✉️ ashwa@example.com | Instagram | Facebook</p>
      </footer>
    </div>
  );
}

export default App;
