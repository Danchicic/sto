import React from 'react';
import axios from "axios";
import host from "../shared/api.js";
import Button from "./UI/Button.jsx";

const TabsSection = ({ active, onChange }) => {
    // Единый обработчик клика по вкладке
    const handleTabClick = async (tabName) => {
        // Специфичная логика для каждой вкладки
        switch (tabName) {
            case "BuyersWithParams":
                // await axios.get(`${host}/...`);
                break;
            case "BuyersByModels":
                // await axios.get(`${host}/...`);
                break;
            case "AutoLess30":
            case "NewAutos":
            case "Liquidity":
            case "MostExpensive":
                // Логика для других вкладок
                break;
            default:
                break;
        }

        // Обновляем активную вкладку
        onChange(tabName);
    };

    // Конфигурация вкладок
    const tabs = [
        { name: "BuyersWithParams", label: "Покупатели по параметрам" },
        { name: "BuyersByModels", label: "Покупатели по модели" },
        { name: "AutoLess30", label: "Авто < 30 тыс. км" },
        { name: "NewAutos", label: "Новые авто" },
        { name: "Liquidity", label: "Соотношение цен" },
        { name: "MostExpensive", label: "Самый дорогой авто" }
    ];

    return (
        <section className="mb-3">
            {tabs.map(tab => (
                <Button
                    key={tab.name}
                    onClick={() => handleTabClick(tab.name)}
                    className={active === tab.name ? "btn-info" : "btn-primary"}
                    dangerouslySetInnerHTML={{ __html: tab.label }}
                />
            ))}
        </section>
    );
};

export default TabsSection;