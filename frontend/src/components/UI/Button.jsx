import React from 'react';


const Button = (params) => {
    let classNames = "btn me-2";
    if (params.className) {
        classNames += " " + params.className;
    }
    return (
        <button {...params} className={classNames}>{params.children}</button>
    );
};

export default Button;