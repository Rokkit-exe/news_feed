import React from 'react';
import { CardActionArea, Grid, Card, CardContent, CardMedia, Typography } from '@mui/material';
import { useMediaQuery, useTheme } from '@mui/material';
import { Link } from 'react-router-dom';


function NewsCard({news}) {
    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

    return (
        <Grid item xs={isMobile ? 12 : 6}>
            <Card sx={{ margin: "1rem", backgroundColor: "background.darker"}} onClick={() => console.log()}>
                <Link to={`/news/${news._id}`} style={{ textDecoration: "none", color: "inherit"}}>
                <CardActionArea>
                    <CardMedia
                        component="img"
                        sx={{
                            /* width: "80%", */
                            padding: "0.5rem"
                        }}
                        image={news.top_image}
                        alt="green iguana"
                    />
                    <CardContent>
                    <Typography gutterBottom variant="h5" component="div" color="text.primary">
                        {news.title}
                    </Typography>
                    <Grid container spacing={2} direction="column" padding={2} marginTop={2}>
                        <Typography variant="body2" color="text.secondary">
                            Date: {news.date}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                            Source: {news.publisher.title}
                        </Typography>
                    </Grid>
                    </CardContent>
                </CardActionArea>
                </Link>
            </Card>
        </Grid>
    )
}

export default NewsCard