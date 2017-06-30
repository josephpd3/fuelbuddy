import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'react-router-redux';
import store, { history } from './store';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import App from './containers/app';

import registerServiceWorker from './registerServiceWorker';

import './index.css';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';

const target = document.querySelector('#root');

render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <div>
        <MuiThemeProvider>
          <App />
        </MuiThemeProvider>
      </div>
    </ConnectedRouter>
  </Provider>,
  target
);

registerServiceWorker();