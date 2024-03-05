import React from "react";
import { AppBar, Toolbar, Button, Box} from "@mui/material";
import LiveTvIcon from "@mui/icons-material/LiveTv";
import RecentActorsIcon from "@mui/icons-material/RecentActors";
import NewspaperIcon from '@mui/icons-material/Newspaper';
import FeedIcon from '@mui/icons-material/Feed';
import CableIcon from '@mui/icons-material/Cable';

import SearchBar from "./search/SearchBar";
import { Link } from "react-router-dom";
import { useMediaQuery, useTheme } from '@mui/material';



function Header() {

    const theme = useTheme();
    const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

    return (
        <AppBar position="static">
            <Toolbar>
                <Button component={Link} to="/" startIcon={<NewspaperIcon />} sx={{ marginX: 1 }} color="inherit">
                    {!isMobile && 'News Feed'}
                </Button>
                <Button component={Link} to="/news" startIcon={<FeedIcon />} sx={{ marginX: 2 }} color="inherit">
                    {!isMobile && 'Feed'}
                </Button>
                <Button component={Link} to="/technews" startIcon={<CableIcon />} sx={{ marginX: 2 }} color="inherit">
                    {!isMobile && 'Tech News'}
                </Button>
                <Box sx={{ flexGrow: 1 }} />
                <SearchBar />
            </Toolbar>
        </AppBar>
    );
}

export default Header;
