<template>
  <div>
    <el-table-v2
      :columns="columns"
      :data="data"
      :width="700"
      :height="400"
      fixed
    />
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


const dummyData = `[{
  "bookName":{"text":"大奉打更人","url":"https://book.qidian.com/info/1019664125/?source=m_jump","img":"https://bookcover.yuewen.com/qdbimg/349573/1019664125/180"},
  "author": {
    "text":"卖报小郎君",
    "url":"https://my.qidian.com/author/9639927/"
  },
  "source":{
    "url":"https://book.qidian.com/info/1019664125/?source=m_jump",
    "text":"起点"
  },
  "tags":["后宫","多女主","仙侠"]
},
  {
    "bookName":{"text":"乱世书","url":"https://book.qidian.com/info/1036010291/","img":"https://bookcover.yuewen.com/qdbimg/349573/1036010291/180"},
    "author": {
      "url":"https://my.qidian.com/author/4173071/",
      "text":"姬叉"
    },
    "source":{
      "url":"https://book.qidian.com/info/1036010291/",
      "text":"起点"
    },
    "tags":["后宫","多女主","玄幻"]
  },
  {
    "bookName":{"text":"问道红尘","url":"https://book.qidian.com/info/1014243481/","img":"https://bookcover.yuewen.com/qdbimg/349573/1014243481/180"},
    "author": {
      "url":"https://my.qidian.com/author/4173071/",
      "text":"姬叉"
    },
    "source":{
      "url":"https://book.qidian.com/info/1014243481/",
      "text":"起点"
    },
    "tags":["后宫","多女主","仙侠"]
  }]`

const dummyData_ = JSON.parse(dummyData);


let id = 0

const dataGenerator = () => ({
  id: `random-id-${++id}`,
  name: 'Tom',
  date: '2020-11-1',
})

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
        return h(ElTag,{class:"mx-1","closable":true,"round":true},{default:()=>tag})
      }),
    ),
  },
  // {
  //   key: 'operations',
  //   title: 'Operations',
  //   cellRenderer: () => (
  //     <>
  //       <ElButton size="small">Edit</ElButton>
  //       <ElButton size="small" type="danger">
  //         Delete
  //       </ElButton>
  //     </>
  //   ),
  //   width: 150,
  //   align: 'center',
  // },
];

// const data = ref(Array.from({ length: 20000 }).map(dataGenerator))
const data = ref(Array.from(dummyData_))
console.log(data);
</script>

<style>
</style>
