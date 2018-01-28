import React, { Component } from 'react';
import SearchBar from './SearchBar';
import './Header.css';

class Header extends Component {

    render() {
        return(
            <div className="Header">
                <div className="Header-title">
                    <h1>News Aggregator</h1>
                    <SearchBar />
                </div>
            </div>
        );
    }
}

export default Header;
