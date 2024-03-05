import React from 'react'
import SearchIcon from '@mui/icons-material/Search';
import SearchIconWrapper from './SearchIconWrapper';
import Search from './Search';
import StyledInputBase from './StyledInputBase';

function SearchBar() {
    return (
        <Search >
            <SearchIconWrapper>
                <SearchIcon />
            </SearchIconWrapper>
            <StyledInputBase/>
        </Search>
    )
}

export default SearchBar