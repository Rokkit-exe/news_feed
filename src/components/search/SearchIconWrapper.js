import React from 'react'
import { styled } from '@mui/material/styles';


function SearchIconWrapper({children}) {
    const SearchIconWrapper = styled("div")(({ theme }) => ({
        padding: theme.spacing(0, 2),
        height: "100%",
        position: "absolute",
        pointerEvents: "none",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    }));

    return (
        <SearchIconWrapper>
            {children}
        </SearchIconWrapper>
    )
}

export default SearchIconWrapper