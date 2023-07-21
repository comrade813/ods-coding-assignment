import Select from 'react-select'
import './dropdown.css';
import { Ref } from 'react';

interface DropdownProps {
    options: Array<Object>,
    val: Ref<any>
}

function Dropdown(props: DropdownProps) {
    return (
        <Select
            className="select"
            options={props.options}
            isClearable={true}
            isSearchable={true}
            placeholder="Select Airport"
            ref={props.val}
        />
      );
}

export default Dropdown;