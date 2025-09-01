import React, { useEffect, useState } from 'react';
import { getUserProfile } from '../services/api';
import Card from '../components/Card';

const Profile = () => {
    const [user, setUser] = useState(null);
    const [favorites, setFavorites] = useState([]);

    useEffect(() => {
        const fetchUserProfile = async () => {
            try {
                const profileData = await getUserProfile();
                setUser(profileData.user);
                setFavorites(profileData.favorites);
            } catch (error) {
                console.error('Error fetching user profile:', error);
            }
        };

        fetchUserProfile();
    }, []);

    if (!user) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{user.username}'s Profile</h1>
            <h2>Favorites</h2>
            <div className="favorites">
                {favorites.map((item) => (
                    <Card key={item.id} item={item} />
                ))}
            </div>
        </div>
    );
};

export default Profile;