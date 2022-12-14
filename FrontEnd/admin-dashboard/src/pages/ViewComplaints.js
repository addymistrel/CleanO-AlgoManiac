import React from "react";
import { useState } from "react";
import { Table } from "antd";

const ViewComplaints = () => {
  const [selectedRowKeys, setSelectedRowKeys] = useState([]);
  const onSelectChange = (newSelectedRowKeys) => {
    console.log("selectedRowKeys changed: ", newSelectedRowKeys);
    setSelectedRowKeys(newSelectedRowKeys);
  };
  const rowSelection = {
    selectedRowKeys,
    onChange: onSelectChange,
    selections: [
      Table.SELECTION_ALL,
      Table.SELECTION_INVERT,
      Table.SELECTION_NONE,
      {
        key: "odd",
        text: "Select Odd Row",
        onSelect: (changableRowKeys) => {
          let newSelectedRowKeys = [];
          newSelectedRowKeys = changableRowKeys.filter((_, index) => {
            if (index % 2 !== 0) {
              return false;
            }
            return true;
          });
          setSelectedRowKeys(newSelectedRowKeys);
        },
      },
      {
        key: "even",
        text: "Select Even Row",
        onSelect: (changableRowKeys) => {
          let newSelectedRowKeys = [];
          newSelectedRowKeys = changableRowKeys.filter((_, index) => {
            if (index % 2 !== 0) {
              return true;
            }
            return false;
          });
          setSelectedRowKeys(newSelectedRowKeys);
        },
      },
    ],
  };
  const columns = [
    {
      title: "Name",
      dataIndex: "name",
      filters: [
        {
          text: "Ram",
          value: "Ram",
        },
        {
          text: "Sham",
          value: "Sham",
        },
        {
          text: "Submenu",
          value: "Submenu",
          children: [
            {
              text: "Green",
              value: "Green",
            },
            {
              text: "Black",
              value: "Black",
            },
          ],
        },
      ],
      // specify the condition of filtering result
      // here is that finding the name started with `value`
      onFilter: (value, record) => record.name.indexOf(value) === 0,
      sorter: (a, b) => a.name.length - b.name.length,
      sortDirections: ["descend"],
    },
    {
      title: "House Id",
      dataIndex: "houseId",
      defaultSortOrder: "descend",
      sorter: (a, b) => a.age - b.age,
    },
    {
      title: "Address",
      dataIndex: "address",
      defaultSortOrder: "descend",
      sorter: (a, b) => a.age - b.age,
    },
    {
      title: "Complaint",
      key: "complaint",
      dataIndex: "complaint",
    },
  ];
  const data = [
    {
      key: "1",
      name: "Ram",
      houseId: 11101,
      address: "unit-1",
      complaint: "Garbage Picker Came Late.",
    },
    {
      key: "2",
      name: "Sham",
      houseId: 11102,
      address: "unit-2",
      complaint: "Grabage haven't been cleaned yet near me.",
    },
    {
      key: "3",
      name: "Rohan",
      houseId: 11103,
      address: "unit-3",
      complaint: "Dump of wet Wastes eradicates Foul Smell.",
    },
    {
      key: "4",
      name: "Nitin",
      houseId: 11104,
      address: "unit-4",
      complaint: "Dustbins are not recycled on Time.",
    },
  ];
  // const ViewComplaints = () => {
  return (
    <Table rowSelection={rowSelection} columns={columns} dataSource={data} />
  );
};

export default ViewComplaints;
