import React, { Component } from 'react';

const BASE_URL = 'https://idmabf73da.execute-api.us-east-1.amazonaws.com/dev'

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      query: null,
      articles: [],
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.fetchData = this.fetchData.bind(this);
  }

  fetchData(query) {
    let invalid_query = true;
    if (query !== null && query !== '' && query !== undefined) {
      invalid_query = false;
    }
    const endpoint = invalid_query ? BASE_URL + '/top' : BASE_URL + `/query?query=${query}`;
    fetch(endpoint)
      .then((response) => response.json())
      .then((data) => {
        this.setState({ articles: data, query: query }, () => {
        });
      });
  }


  componentWillMount() {
    this.fetchData();
  }

  handleChange(event) {
    this.setState({ query: event.target.value });
  }

  handleSubmit(event) {
    event.preventDefault();
    this.fetchData(this.state.query)
  }

  render() {
    const articles = this.state.articles;
    const listItems = articles !== undefined ? articles.map((d) =>
      <li key={d.title}>
        <p>
          This article from {d.publication} is most likely {d.articleBias}: <a href={d.url}>{d.title}</a>
        </p>
      </li>
    ): [];
    return (
      <div>
        <nav className="navbar navbar-default">
          <div className="container-fluid">
            <div className="navbar-header">
              <button type="button" className="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span className="sr-only">Toggle navigation</span>
                <span className="icon-bar"></span>
                <span className="icon-bar"></span>
                <span className="icon-bar"></span>
              </button>
              <a className="navbar-brand" href="#">Know Your News</a>
            </div>
            <div className="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
              <form className="navbar-form navbar-left" onSubmit={this.handleSubmit}>
                <div className="form-group">
                  <input type="text" className="form-control" placeholder="Search For Articles" value={this.state.value} onChange={this.handleChange} />
                </div>
                <button type="submit" className="btn btn-default">Search</button>
              </form>
              <ul className="nav navbar-nav navbar-right">
                <li><a href="#">Link</a></li>
              </ul>
            </div>
          </div>
        </nav>
        <div>
          <h2 className="text-center"> KNOW YOUR NEWS</h2>
          <h4 className="text-center"> A Selection of Today's Top Articles</h4>
          <div style={{ marginTop: "40" }}>
            <ul style={{ marginLeft: "30", listStyle: 'none' }}>
              {listItems}
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
