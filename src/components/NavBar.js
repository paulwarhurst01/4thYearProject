import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon  from '@material-ui/icons/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Menu from '@material-ui/core/Menu';

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
  const classes = useStyles();

  const [anchorEl, setAnchorEI] = React.useState(null);

  const handleClick = (event) => {
    setAnchorEI(event.currentTarget);
  };

  const handleClose = () => {
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
              <MenuItem onClick={handleClose}>Perform Lidar Scan</MenuItem>
              <MenuItem onClick={handleClose}>Reset Arduinos</MenuItem>
              <MenuItem onClick={handleClose}>Reset Motor Control</MenuItem>
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