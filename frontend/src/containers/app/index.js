import React from 'react';
import { Route, Link } from 'react-router-dom';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import FlatButton from 'material-ui/FlatButton';
import Map from './../map';
import Admin from './../admin';

const styles = {
  title: {
    color: 'white',
  },
};

const App = () => (
  <div>
    <AppBar
        title={<span style={styles.title}>FuelBuddy</span>}
        iconElementRight={<FlatButton label="Login" />}
        iconElementLeft={<span></span>}
    />
    <Route exact path="/" component={Map} />
    <Route exact path="/admin" component={Admin} />
  </div>
)

export default App;