import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon  from '@material-ui/icons/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';

// HOOK
import hookContext from '../hooks';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function NavBar() {
  const { lidarCall, resetArduino, resetMotors} = hookContext();
  const classes = useStyles();

  const [anchorEl, setAnchorEI] = React.useState(null);

  const handleClick = (event) => {
    setAnchorEI(event.currentTarget);
  };

  const handleClose = async (data) => {
    console.log(typeof lidarCall);
    switch(data){
      case 1: 
        lidarCall();
        break;
      case 2: 
        resetArduino();
        break;

  default: break;
}
setAnchorEI(null);
};

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <div>
            <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
              <MenuIcon onClick={handleClick}/>
            </IconButton>
            <Menu 
              id="menu"
              anchorEl={anchorEl}
              keepmounted
              open={Boolean(anchorEl)}
              onclose={handleClose}
            >
              <MenuItem onClick={handleClose}>Close Menu</MenuItem>
              <MenuItem onClick={() => handleClose(1)}>Perform Lidar Scan</MenuItem>
              <MenuItem onClick={() => handleClose(2)}>Reset Arduino</MenuItem>
            </Menu>
          </div>
          <Typography variant="h6" className={classes.title}>
           Robot Control Centre
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}