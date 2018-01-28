import React, { Component } from 'react';

class Top extends Component {
    constructor() {
        super();
        this.state = {
            articles: [],
        };
    }

    componentDidMount() {
        fetch('https://idmabf73da.execute-api.us-east-1.amazonaws.com/dev/top')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            this.setState({articles: data});
        });
    }

    render() {
        const articles = this.state.articles;
        const listItems = articles.map( (d) =>
            <li key={d.title}>
                <p>This article from {d.publication} is most likely {d.articleBias}: </p>
                <a href={d.url}>{d.title}</a>
            </li>
        );
        return (
            <div>
                {listItems}
            </div>
        );
    }
}

export default Top;
