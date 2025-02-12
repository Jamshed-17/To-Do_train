import logo from './logo.svg';
import './App.css';
import { useEffect, useState, setState } from 'react';
import axios from 'axios';

const MyInput = () => {
    const [value, setValue] = useState('');
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        const response = axios
            .get("http://193.107.238.171/api/get")
            .then((response) => setTodos(response.data))
        
    }, [])

    const InputChange = (event) => {
        setValue(event.target.value);
    }

    const PostData = async (index, todo) => {
        try {
            const response = await axios.post("http://193.107.238.171/api/create", { id: index, name: todo });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }

    }

    const ButtonChange = async () => { 
        if (value !== "") {
            await PostData(todos.length + 1, value);
            setValue("");
            window.location.reload() 
        }
    }
    

    const deleteTodo = async (index) => {
        const response = await axios.post(`http://193.107.238.171/api/remove/${index}`)
        console.log(response.data);
        const newTodos = todos.filter((item) => item !== index);
        setTodos(newTodos);
        window.location.reload(); 
    }

    return (
        <>
            <div className="add">
                <input className="input" type="text" onChange={InputChange} value={value}/>
                <button type="button" className="add-button" onClick={ButtonChange}>Добавить</button>
            </div>
            <div className='todo-list'>
            <ol>
                {todos && todos.map((todo, index) => (
                    <li className='todo' key={todo.id}>
                        <span>{todo.name}</span>
                        <button type="button" className='delete-button' onClick={() => { deleteTodo(todo.id)}}>Удалить</button>
                    </li>
                ))}
            </ol>
            </div>
            
        </>
    )
}

export default MyInput;