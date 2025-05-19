import React, {useState} from 'react';
import BuyersWithParams from "../components/queries/BuyersWithParams.jsx";
import TabsSection from "../components/TabsSection.jsx";
import BuyersByModels from "../components/queries/BuyersByModels.jsx";

function QueriesPage() {
    const [chosenQuery, setChosenQuery] = useState("BuyersWithParams");

    const changeQuery = (current) => {
        setChosenQuery(current);
    }

    const componentsConfiguration = {
        "BuyersWithParams": <BuyersWithParams key={1}/>,
        "BuyersByModels": <BuyersByModels key={2}/>,
    }

    return (
        <div>
            <h2>Запросы</h2>
            <TabsSection active={chosenQuery} onChange={changeQuery}/>
            {Object.entries(componentsConfiguration).map(([tabName, component]) => {
                if (tabName === chosenQuery) {

                    return (component)
                }
            })}
        </div>
    );
}

export default QueriesPage;