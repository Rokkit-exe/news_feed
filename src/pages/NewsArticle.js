import React, {useEffect, useState} from 'react'
import { Container, Grid, Card, CardContent, CardMedia, Typography } from '@mui/material'
import { Link, useParams } from 'react-router-dom'
import Header from '../components/Header'
import axios from 'axios'

function NewsArticle() {
    const { id } = useParams();
    console.log(id)

    const [news, setNews] = useState([]); // state to store the news

    useEffect(() => {
        axios.get(`http://localhost:5000/fetch_by_id/${id}`)
            .then(response => {
                console.log("news: ", response.data.news)
                setNews(response.data.news); // update the state with the fetched data
            })
            .catch(error => {
                console.error('There was an error!', error);
            });
    }, [id]);
    if (!news) {
        return (
            <>
                <Typography variant="h1" color={"text.dark"}>Loading...</Typography>
            </>
        )
    }
    else {
        return (
            <>
                <Header />
                <Container>
                    <Grid container spacing={2} marginTop={2}>
                        <Card sx={{ margin: "1rem", backgroundColor: "background.darker"}}>
                            <CardMedia
                                component="img"
                                sx={{
                                    padding: "0.5rem"
                                }}
                                image={news.top_image}
                                alt="green iguana"
                            />
                            <CardContent>
                                <Typography gutterBottom variant="h5" component="div" color="white" fontSize={32}>
                                    {news.title && news.title}
                                </Typography>
                                <Typography variant="body1" color="text.primary">
                                    {news.text && news.text.split('\n').map((line, index) => (
                                        <React.Fragment key={index}>
                                            {line}
                                            <br />
                                        </React.Fragment>
                                    ))}
                                </Typography>
                                <Grid container spacing={2} direction="column" padding={2} marginTop={2}>
                                    <Typography variant="body2" color="text.secondary">
                                        Date: {news.date}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                        Source: 
                                    </Typography>
                                    <Grid container spacing={2} direction="row" padding={2} marginTop={2}>
                                        <Typography variant="body2" color="text.secondary">
                                            original article: 
                                        </Typography>
                                        <Link to={news.url} >
                                            <Typography variant="body2" marginLeft={2}>
                                                {news.url} 
                                            </Typography>
                                        </Link>
                                    </Grid>
                                </Grid>
                            </CardContent>
                        </Card>
                    </Grid>
                </Container>
            </>
            
        )
    }
}

export default NewsArticle