import React from 'react'
import { alpha, styled } from '@mui/material/styles';

function Search({children}) {
    const Search = styled("div")(({ theme }) => ({
        position: "relative",
        justifyItems: "flex-end",
        borderRadius: theme.shape.borderRadius,
        backgroundColor: alpha(theme.palette.common.white, 0.15),
            "&:hover": {
        backgroundColor: alpha(theme.palette.common.white, 0.25),
        },
        marginLeft: 0,
        width: "100%",
        [theme.breakpoints.up("sm")]: {
        marginLeft: theme.spacing(1),
        width: "auto",
        },
    }));
    return (
        <Search>
            {children}
        </Search>
    )
}

export default Search