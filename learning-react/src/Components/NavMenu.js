import React from 'react';
import { Link } from 'react-router-dom';

function NavMenu(props) {
    return (
        <div>
          <div className="font-bold py-3">
            This is the Menu
          </div>
          <ul >
            <li><Link
                  to="/"
                  onClick={props.closeMenu}
                  className="text-blue-500 py-3 border-t border-b block"
                >
                  Home
                </Link>
            </li>
            <li><Link
                  to="/about"
                  onClick={props.closeMenu}
                  className="text-blue-500 py-3 border-b block"
                >
                  About
                </Link>
            </li>
          </ul>
        </div>
    );
}

export default NavMenu
