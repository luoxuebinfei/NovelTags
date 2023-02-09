<template>
  <div>
    <el-table-v2
      :columns="columns"
      :data="data"
      :width="1200"
      :height="400"
      fixed
    />
    <el-button @click="getData">刷新</el-button>
  </div>
</template>

<script setup lang="tsx">
import {h, ref} from 'vue'
import dayjs from 'dayjs'
import {
  ElButton,
  ElIcon,
  ElTag,
  ElTooltip,
  TableV2FixedDir,
} from 'element-plus'
import { Timer } from '@element-plus/icons-vue'

import type { Column } from 'element-plus'
import * as stream from "stream";

import {GetData} from "../http/api/user.js"

const data = ref([])



//获取表格数据
const getData = async ()=>{
  await GetData().then((res) => {
    data.value=res as Array<any>;
})}

getData()


const columns: Column<any>[] = [
  {
    key: 'bookName',
    title: '书名',
    dataKey: 'bookName',
    width: 150,
    fixed: TableV2FixedDir.LEFT,
    cellRenderer: ({ cellData: bookName }) => (
      <ElTooltip content={bookName["text"]}>
        {
          <span class="flex items-center">
            <a href={bookName["url"]}>{bookName["text"]}</a>
          </span>
        }
      </ElTooltip>
    ),
  },
  {
    key: 'author',
    title: '作者',
    dataKey: 'author',
    width: 150,
    align: 'center',
    cellRenderer: ({ cellData: author }) => <ElTooltip content={author["text"]}><a href={author["url"]}>{author["text"]}</a></ElTooltip>,
  },
  {
    key: 'source',
    title: '发布平台',
    dataKey: 'source',
    width: 150,
    align: 'center',
    cellRenderer: ({ cellData: source }) => <ElTooltip content={source["text"]}><a href={source["url"]}>{source["text"]}</a></ElTooltip>,
  },
  {
    key: 'tags',
    title: '标签',
    dataKey: 'tags',
    width: 350,
    align: 'center',
    cellRenderer: ({ cellData:tags}) => h(
      "div",
      {},
      tags.map((tag)=>{
        return h(ElTag,{class:"mx-1","closable":true,"round":true,onClose:()=>{}},{default:()=>tag})
      }),
    ),
  },
];

</script>

<style>
</style>
