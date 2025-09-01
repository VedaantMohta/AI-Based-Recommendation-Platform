import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Card from '../components/Card';

const Home = () => {
    const [items, setItems] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchItems = async () => {
            try {
                const response = await axios.get('/api/items'); // Adjust the endpoint as necessary
                setItems(response.data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchItems();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Recommended Items</h1>
            <div className="item-list">
                {items.map(item => (
                    <Card key={item.id} item={item} />
                ))}
            </div>
        </div>
    );
};

export default Home;