import './table.css'

interface TableProps {
    data: Array<Array<string>>
}

function Table(props: TableProps) {
    return (
        <div className="App">
            <table>
                <tbody>
                <tr>
                    <th>flt_num</th>
                    <th>origin_gate</th>
                    <th>dest_gate</th>
                    <th>out_gmt</th>
                    <th>in_gmt</th>
                    <th>off_gmt</th>
                    <th>on_gmt</th>
                    <th>origin</th>
                    <th>destination</th>
                </tr>
                {props.data.map((arr: Array<string>) => {
                    return (
                        <tr key={arr[0]}>
                            <td>{arr[1]}</td>
                            <td>{arr[2]}</td>
                            <td>{arr[3]}</td>
                            <td>{arr[4]}</td>
                            <td>{arr[5]}</td>
                            <td>{arr[6]}</td>
                            <td>{arr[7]}</td> 
                            { arr[11] === null ?
                                <td>{arr[9]}</td> :
                                <td>{arr[11]} ({arr[9]})</td>
                            }
                            { arr[10] === null ?
                                <td>{arr[8]}</td> :
                                <td>{arr[10]} ({arr[8]})</td>
                            }
                        </tr>
                    )
                })}
                </tbody>
            </table>
        </div>
    );
}

  export default Table;