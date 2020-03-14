<template lang="pug">
section#home-reservation.section
  div.container
    h2.title レビュー状況
    table.table
      thead
        tr
          th ステータス
          th 牌譜URL
          th 予約時刻
      tbody
        tr(v-for="(review, i) in reviewList" :key="i")
          td {{ review.reviewStatus }}
          td {{ review.mjlogWatchUrl }}
          td {{ review.reservedAt }}
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator"
import axios, { AxiosResponse } from "axios"
import moment from "moment"

interface ReviewModel {
  review_status: 1 | 2 | 3 | 4
  mjlog_watch_url: string
  reserved_at: string
}

interface Review {
  reviewStatus: string
  mjlogWatchUrl: string
  reservedAt: string
}

@Component
export default class HomeReview extends Vue {
  reviewList: Review[] = []

  created() {
    this.fetchReviewListAsync().then((data) => {
      this.reviewList = data
    })
  }

  async fetchReviewListAsync(): Promise<Review[]> {
    const res: AxiosResponse<ReviewModel[]> = await axios.get(
      "/api/review/list"
    )
    return res.data.map(
      (x: ReviewModel): Review => {
        const ReviewStatus = { 1: "⌛", 2: "🔃", 3: "✅", 4: "⚠" }
        return {
          reviewStatus: ReviewStatus[x.review_status],
          mjlogWatchUrl: x.mjlog_watch_url,
          reservedAt: moment(x.reserved_at).format("YYYY/MM/DD HH:mm:ss")
        }
      }
    )
  }
}
</script>

<style lang="stylus" scoped></style>
