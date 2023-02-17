# Load something as data is being fetched

1.  `const [cargado, setCargado] = useState(false)`
2.  ```
    useEffect(()=>{

    },[])
    ```

3.  HTML

            <Card.Img
                variant="top"
                {if (cargado = false) {
                    // Display this 'loading' image
                    } else {
                    // Display the 'real' image

    }
    ...
