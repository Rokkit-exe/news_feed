import React, {useEffect, useState} from 'react'
import Header from '../components/Header'
import { Grid, Container } from '@mui/material'
import NewsCard from '../components/NewsCard'
import axios from 'axios'

function NewsFeed() {

    const [newsList, setNewsList] = useState([]); // state to store the news

    useEffect(() => {
        axios.get('http://localhost:5000/fetch_by_date_dsc')
            .then(response => {
                setNewsList(response.data.news); // update the state with the fetched data
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
    }, []);

    console.log(newsList[0])

    return (
        <>
            <Header />
            <Container >
                <Grid container spacing={2} >
                    {newsList.map((news, index) => <NewsCard key={index} news={news} />)}
                </Grid>
            </Container>
        </>
    )
}

export default NewsFeed