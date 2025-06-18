// CarList.test.jsx
import React from "react";
import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom"; // <-- Добавлено
import axios from "axios";

import CarList from "./CarList";

// В начале файла, сразу после импортов
jest.mock('../shared/api.js', () => ({
  default: 'http://localhost:8000',
}));
jest.mock("axios");

const mockCars = [
    {
        id: 1,
        company: { name: "Toyota" },
        model: { name: "Camry" },
        year: 2020,
        engine_power: 200,
        transmission_type: { name: "Автомат" },
        auto_type: { name: "Новое" },
        cost: 25000,
        is_reserved: false,
    },
    {
        id: 2,
        company: { name: "Honda" },
        model: { name: "Civic" },
        year: 2019,
        engine_power: 180,
        transmission_type: { name: "Механика" },
        auto_type: { name: "Б/у" },
        cost: 20000,
        is_reserved: true,
    },
];

describe("CarList Component", () => {
    beforeEach(() => {
        axios.get.mockClear();
        axios.delete.mockClear();
        axios.patch.mockClear();
        localStorage.clear();
    });

    test("рендерит заголовок и таблицу", () => {
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );
        expect(screen.getByText(/Список автомобилей/i)).toBeInTheDocument();
        expect(screen.getByRole("table")).toBeInTheDocument();
    });

    test("загружает автомобили из API и отображает их", async () => {
        // axios.get.mockResolvedValue({ data: { cars: mockCars } });
        axios.get.mockResolvedValueOnce({ data: { cars: mockCars } });
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );

        await waitFor(() => {
            expect(screen.getByText("Toyota")).toBeInTheDocument();
            expect(screen.getByText("Honda")).toBeInTheDocument();
        });
    });

    // Обновите все остальные тесты аналогично, обернув <CarList /> в <MemoryRouter>

    test("отображает данные автомобиля", async () => {
        axios.get.mockResolvedValue({ data: { cars: [mockCars[0]] } });
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );

        await waitFor(() => {
            expect(screen.getByText("Camry")).toBeInTheDocument();
            expect(screen.getByText("2020")).toBeInTheDocument();
            expect(screen.getByText("200")).toBeInTheDocument();
            expect(screen.getByText("Автомат")).toBeInTheDocument();
            expect(screen.getByText("Новое")).toBeInTheDocument();
            expect(screen.getByText("25000")).toBeInTheDocument();
        });
    });

    test('отображает кнопку "Купить" для пользователя', async () => {
        localStorage.setItem("role", "user");
        axios.get.mockResolvedValue({ data: { cars: [mockCars[0]] } });
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );

        await waitFor(() => {
            expect(
                screen.getByRole("button", { name: /Купить/i })
            ).toBeInTheDocument();
        });
    });

    test('отображает кнопку "Куплено" для забронированного авто', async () => {
        localStorage.setItem("role", "user");
        axios.get.mockResolvedValue({ data: { cars: [mockCars[1]] } });
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );

        await waitFor(() => {
            expect(
                screen.getByRole("button", { name: /Куплено/i })
            ).toBeInTheDocument();
        });
    });

    test('отображает кнопку "Удалить" для магазина', async () => {
        localStorage.setItem("role", "shop");
        axios.get.mockResolvedValue({ data: { cars: [mockCars[0]] } });
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );

        await waitFor(() => {
            expect(
                screen.getByRole("button", { name: /Удалить/i })
            ).toBeInTheDocument();
        });
    });

    
    
    test("не позволяет забронировать уже купленный авто", async () => {
        localStorage.setItem("role", "user");
        axios.get.mockResolvedValue({ data: { cars: [mockCars[1]] } });
        render(
            <MemoryRouter>
                <CarList />
            </MemoryRouter>
        );

        const button = await screen.findByRole("button", { name: /Куплено/i });
        expect(button).toBeDisabled();
    });
});
