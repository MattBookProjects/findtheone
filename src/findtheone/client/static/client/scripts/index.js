class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {page: <LoginPage/>}
    }

    render(){
        return (
            <div className="app">
                {this.state.page}
            </div>
        );
    }
}

function Button(props) {
    return (
        <button className={props.className} onClick={props.onClick}>{props.label}</button>
    );
}

function TextInput(props){
    return(
        <input type="text" placeholder={props.placeholder} value={props.value} onChange={props.onChange}/>
    );
}

class LoginPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {username: "", password: ""};
        this.handleUsernameChange = this.handleUsernameChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }


    render() {
        return (
           <div className="login-page">
              <input type="text" value={this.state.username} onChange={this.handleUsernameChange} placeholder="Username"/>
              <input type="password" value={this.state.password} onChange={this.handlePasswordChange} placeholder="Password"/>
              <Button onClick={this.handleSubmit} label="Login"/>
           </div>
        )
    }

    handleUsernameChange(event){
        this.setState({username: event.target.value});
    }

    handlePasswordChange(event){
        this.setState({password: event.target.value});
    }

    handleSubmit(event){
        ;
    }

}