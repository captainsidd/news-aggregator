import React, { Component } from 'react';

class Top extends Component {
    constructor() {
        super();
        this.state = {
            articles: [],
        };
    }

    componentDidMount() {
        fetch('https://qtufv0jykg.execute-api.us-east-1.amazonaws.com/dev/top', {headers: {'Content-Type': 'application/json'}})
        .then((response) => response.json())
        .then(function(data) {
            console.log(data.results);
        });
    }

    render() {
        return (
            <p>Hello</p>
        );
    }
}

export default Top;
