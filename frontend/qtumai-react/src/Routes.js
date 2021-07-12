import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Main from "./pages/Main/Main";
import Login from './pages/Login/Login';
import Signup from './pages/Signup/Signup';
import SignupNext from './pages/Signup/SignupNext/SignupNext';
import Profile from './pages/Profile/Profile';

class Routes extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={Main} />
          <Route exact path="/login" component={Login} />
          <Route exact path="/signup" component={Signup} />
          <Route exact path="/signup/next" component={SignupNext} />
          <Route exact path="/profile" component={Profile} />
        </Switch>
      </Router>
    );
  }
}
export default Routes;
