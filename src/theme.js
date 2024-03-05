import { createTheme } from '@mui/material/styles';

// A custom theme for this app
const theme = createTheme({
    palette: {
        primary: {
            main: '#212529',
        },
        secondary: {
            main: '#3f454d',
        },
        background: {
            default: '#212529',
            dark: '#212529',
            darker: '#161b22',
            grey: '#424549',
        },
        text: {
            primary: '#f8f9fa',
            secondary: '#adb5bd',
            light: '#f8f9fa',
            dark: '#212529',
            main: '#adb5bd',
        },
        success: {
            light: '#81c784',
            main: '#4caf50',
            dark: '#388e3c',
            contrastText: 'rgba(0, 0, 0, 0.87)',
        },
    },
});

export default theme;